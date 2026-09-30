const DEFAULT_API = `${window.location.origin}/api`;
const API_KEY = 'bis_recommender_api';

function api() {
  return (localStorage.getItem(API_KEY) || DEFAULT_API).replace(/\/+$/, '');
}
function setApi(u) { localStorage.setItem(API_KEY, u.replace(/\/+$/, '')); }

const $ = id => document.getElementById(id);
const E = {
  connStatus: $('connStatus'), connLabel: $('connLabel'),
  apiUrlInput: $('apiUrlInput'), currentApiUrl: $('currentApiUrl'), saveApiBtn: $('saveApiBtn'),
  statFamilies: $('statFamilies'), statStandards: $('statStandards'),
  statAsOf: $('statAsOf'), footerDate: $('footerDate'),
  exampleButtons: $('exampleButtons'),
  descInput: $('descInput'), charCount: $('charCount'), lineCount: $('lineCount'),
  fileInput: $('fileInput'), fileLabel: $('fileLabel'),
  tenderDate: $('tenderDate'), deliveryDays: $('deliveryDays'),
  deliveryDate: $('deliveryDate'), entSize: $('entSize'),
  analyzeBtn: $('analyzeBtn'), inputErr: $('inputErr'),
  results: $('results'),
  familyBanner: $('familyBanner'), recsList: $('recsList'),
  findingsList: $('findingsList'), certList: $('certList'),
  understoodPanel: $('understoodPanel'), clauseBox: $('clauseBox'),
  copyBtn: $('copyBtn'), printBtn: $('printBtn'),
  disclaimerBar: $('disclaimerBar'),
};

document.addEventListener('DOMContentLoaded', () => {
  E.apiUrlInput.value = api();
  E.currentApiUrl.textContent = api();
  E.saveApiBtn.addEventListener('click', () => { setApi(E.apiUrlInput.value.trim() || DEFAULT_API); checkHealth(); });
  E.descInput.addEventListener('input', updateCounters);
  E.fileInput.addEventListener('change', () => { E.fileLabel.textContent = E.fileInput.files[0]?.name || ''; });
  E.analyzeBtn.addEventListener('click', runAnalysis);
  E.copyBtn.addEventListener('click', () => {
    navigator.clipboard?.writeText(E.clauseBox.value);
    flash(E.copyBtn, '<i class="bi bi-check2 me-1"></i>Copied!');
  });
  E.printBtn.addEventListener('click', () => window.print());
  checkHealth();
  loadExamples();
});

function updateCounters() {
  const t = E.descInput.value;
  E.charCount.textContent = t.length;
  E.lineCount.textContent = t.split('\n').filter(l => l.trim()).length;
}
function flash(btn, html) {
  const orig = btn.innerHTML;
  btn.innerHTML = html;
  setTimeout(() => btn.innerHTML = orig, 1400);
}
function setConn(kind, label) {
  E.connStatus.className = `conn-pill conn-${kind}`;
  E.connLabel.textContent = label;
}
function esc(s) {
  const d = document.createElement('div'); d.textContent = s ?? ''; return d.innerHTML;
}

async function checkHealth() {
  setConn('pending', 'Connecting…');
  try {
    const r = await fetch(`${api()}/health/`);
    if (!r.ok) throw new Error();
    const d = await r.json();
    setConn('ok', 'Connected');
    E.statFamilies.textContent = d.families_seeded ?? '—';
    E.statStandards.textContent = d.standards_seeded ?? '—';
    E.statAsOf.textContent = d.data_as_of ?? '—';
    E.footerDate.textContent = d.data_as_of ?? '—';
    E.currentApiUrl.textContent = api();
  } catch { setConn('fail', 'Backend unreachable'); }
}

async function loadExamples() {
  try {
    const r = await fetch(`${api()}/examples/`);
    const d = await r.json();
    E.exampleButtons.innerHTML = '';
    (d.examples || []).forEach(ex => {
      const btn = document.createElement('button');
      btn.type = 'button'; btn.className = 'btn';
      btn.textContent = ex.label; btn.title = ex.highlights || '';
      btn.addEventListener('click', () => applyExample(ex));
      E.exampleButtons.appendChild(btn);
    });
  } catch { /* silent if backend not up yet */ }
}

function applyExample(ex) {
  E.descInput.value = ex.description; updateCounters();
  E.deliveryDays.value = ex.delivery_period_days || '';
  E.deliveryDate.value = ''; E.tenderDate.value = '';
  E.entSize.value = ex.enterprise_size || 'large';
  E.fileInput.value = ''; E.fileLabel.textContent = '';
  E.descInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

async function runAnalysis() {
  E.inputErr.classList.add('d-none');
  setLoading(true);
  try {
    let res;
    const common = {
      tender_date: E.tenderDate.value || null,
      delivery_date: E.deliveryDate.value || null,
      delivery_period_days: E.deliveryDays.value || null,
      enterprise_size: E.entSize.value,
    };
    if (E.fileInput.files.length) {
      const fd = new FormData();
      fd.append('file', E.fileInput.files[0]);
      fd.append('description', E.descInput.value.trim());
      Object.entries(common).forEach(([k, v]) => v && fd.append(k, v));
      res = await fetch(`${api()}/analyze/`, { method: 'POST', body: fd });
    } else {
      res = await fetch(`${api()}/analyze/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description: E.descInput.value.trim(), ...common }),
      });
    }
    const data = await res.json();
    if (!res.ok) { showErr(data.error || 'Something went wrong.'); return; }
    render(data);
  } catch (e) { showErr('Could not reach the backend. Check the API URL (gear icon, top right).'); }
  finally { setLoading(false); }
}

function showErr(msg) { E.inputErr.textContent = msg; E.inputErr.classList.remove('d-none'); }
function setLoading(on) {
  E.analyzeBtn.disabled = on;
  E.analyzeBtn.querySelector('.label-default').classList.toggle('d-none', on);
  E.analyzeBtn.querySelector('.label-loading').classList.toggle('d-none', !on);
}

function render(data) {
  E.results.classList.remove('d-none');
  renderBanner(data.family_detection);
  renderRecs(data.recommendations, data.family_detection);
  renderFindings(data.findings);
  renderCerts(data.certifications, data.input_summary);
  renderUnderstood(data);
  renderClause(data);
  E.disclaimerBar.textContent = `${data.disclaimer} · Data as of ${data.data_as_of}.`;
  E.results.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function renderBanner(fd) {
  const band = fd.abstained ? 'abstained' : fd.confidence_band;
  const icons = { high: 'bi-check-circle-fill', medium: 'bi-info-circle-fill', abstained: 'bi-exclamation-triangle-fill', none: 'bi-exclamation-triangle-fill' };
  const icon = icons[band] || 'bi-info-circle-fill';
  let title, body;
  if (fd.abstained) {
    title = 'Could not identify a product family';
    body = esc(fd.abstain_reason || '');
  } else {
    const langLabels = { en: 'English', hi: 'Hindi', ta: 'Tamil', te: 'Telugu', kn: 'Kannada', gu: 'Gujarati', mr: 'Marathi' };
    const langLabel = langLabels[fd.detected_language] || fd.detected_language || 'English';
    const expandedNote = fd.was_expanded
      ? `<span class="badge bg-info text-dark ms-2" title="Regional/trade terms detected and expanded to standard English equivalents">🌐 ${langLabel} terms recognised</span>`
      : (fd.detected_language && fd.detected_language !== 'en'
          ? `<span class="badge bg-secondary ms-2">Language: ${langLabel}</span>`
          : '');
    title = `Detected: <strong>${esc(fd.detected_family_name)}</strong> &nbsp;<span class="fw-normal text-muted">(confidence: ${esc(fd.confidence_band)})</span>${expandedNote}`;
    const chips = (fd.matched_keywords || []).map(k => `<span class="kw-chip">${esc(k)}</span>`).join('');
    body = chips ? `Matched on: ${chips}` : 'No specific keywords recorded.';
  }
  E.familyBanner.className = `family-banner band-${band}`;
  E.familyBanner.innerHTML = `<i class="bi ${icon} banner-icon"></i><div><div class="banner-title">${title}</div><div class="mt-1 small">${body}</div></div>`;
}

const ROLE_LABELS = {
  primary: 'Primary', test_method: 'Test method', normative_reference: 'Normative ref.',
  sampling: 'Sampling', safety: 'Safety', installation: 'Installation',
  code_of_practice: 'Code of practice', packaging: 'Packaging', co_cited: 'Related',
};
const STATUS_LABELS = { current: 'Current', withdrawn: 'Withdrawn', superseded: 'Superseded', unknown: 'Unknown' };
const VERDICT_LABELS = {
  mandatory_now: 'Mandatory now',
  mandatory_by_delivery: 'Mandatory by delivery date',
  mandatory_historical_verify_date: 'Historically mandatory — verify date',
  upcoming_after_delivery: 'Upcoming after delivery',
  deferred_or_revoked: 'Deferred / revoked',
  voluntary_or_no_rule_found: 'No mandatory rule found',
};
const FINDING_ICONS = {
  param_conflict: 'bi-rulers', internal_inconsistency: 'bi-exclamation-triangle-fill',
  withdrawn_citation: 'bi-x-octagon-fill', superseded_citation: 'bi-arrow-clockwise',
  year_mismatch: 'bi-calendar-x', missing_primary_standard: 'bi-exclamation-diamond-fill',
  missing_allied: 'bi-link-45deg', possible_wrong_standard: 'bi-question-diamond-fill',
  not_covered: 'bi-database-slash', abstained: 'bi-emoji-neutral',
};

function renderRecs(recs, fd) {
  if (fd.abstained || !recs?.length) {
    E.recsList.innerHTML = '<p class="text-muted small">No recommendations — see the detection banner above.</p>'; return;
  }
  E.recsList.innerHTML = recs.map(r => {
    const statusClass = `is-${r.status}`;
    const isPrimary = r.role === 'primary';
    const roleBadge = `<span class="role-badge role-${r.role}">${ROLE_LABELS[r.role] || r.role}</span>`;
    const mandatoryBadge = r.mandatory && r.role !== 'primary' ? '<span class="mandatory-badge ms-1">Required</span>' : '';
    const statusBadge = `<span class="status-badge status-${r.status}">${STATUS_LABELS[r.status] || r.status}</span>`;
    const verifBadge = `<span class="verif-chip verif-${r.verification}"></span>`;
    const srcLink = r.source_url ? `<a href="${esc(r.source_url)}" target="_blank" rel="noopener" class="ms-1">source ↗</a>` : '';
    const amendBadge = r.amendments?.length ? `<span class="amend-tag ms-1">Amend. ${r.amendments.length}</span>` : '';
    const amendNote = r.amendment_note ? `<div class="text-warning small mt-1"><i class="bi bi-info-circle me-1"></i>${esc(r.amendment_note)}</div>` : '';
    const condNote = r.condition ? `<div class="condition-note mt-1"><i class="bi bi-diagram-2 me-1"></i>Applies when: ${esc(r.condition)}</div>` : '';
    const reasonText = r.reason ? `<div class="mt-1">${esc(r.reason)}</div>` : '';
    const replacedBy = r.replaced_by ? `<div class="text-danger small mt-1"><i class="bi bi-arrow-right-circle me-1"></i>Replaced by: ${esc(r.replaced_by)}</div>` : '';
    return `
    <div class="std-card ${isPrimary ? 'is-primary' : statusClass}">
      <div class="d-flex justify-content-between align-items-start gap-2 flex-wrap">
        <div class="flex-grow-1">
          <div class="d-flex align-items-center gap-2 flex-wrap">
            <span class="std-num">${esc(r.display_number)}</span>
            ${roleBadge}${mandatoryBadge}${statusBadge}${amendBadge}
          </div>
          <div class="std-title">${esc(r.title)}</div>
          <div class="std-meta">
            ${reasonText}${condNote}${replacedBy}${amendNote}
            <div class="mt-1">${verifBadge}${srcLink}</div>
          </div>
        </div>
      </div>
      <div class="fb-row">
        <button class="btn btn-sm btn-outline-success fb-btn" data-is="${esc(r.is_number)}" data-act="accept" title="Mark as helpful"><i class="bi bi-hand-thumbs-up"></i></button>
        <button class="btn btn-sm btn-outline-danger fb-btn" data-is="${esc(r.is_number)}" data-act="reject" title="Mark as incorrect"><i class="bi bi-hand-thumbs-down"></i></button>
        <button class="btn btn-sm btn-outline-warning fb-btn" data-is="${esc(r.is_number)}" data-act="flag" title="Flag for review"><i class="bi bi-flag"></i></button>
      </div>
    </div>`;
  }).join('');
  E.recsList.querySelectorAll('.fb-btn').forEach(btn =>
    btn.addEventListener('click', () => sendFb(btn.dataset.is, btn.dataset.act, btn))
  );
}

async function sendFb(is_number, action, btn) {
  try {
    await fetch(`${api()}/feedback/`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ is_number, action }) });
    btn.innerHTML = '<i class="bi bi-check2"></i>';
    btn.disabled = true;
  } catch { /* best-effort */ }
}

function renderFindings(findings) {
  if (!findings?.length) { E.findingsList.innerHTML = '<p class="text-muted small">No issues found in the curated checks.</p>'; return; }
  E.findingsList.innerHTML = findings.map(f => `
    <div class="finding-card f-${f.severity}">
      <i class="bi ${FINDING_ICONS[f.type] || 'bi-info-circle'}"></i>
      <div>
        <div class="finding-type">${esc(f.type.replace(/_/g, ' '))} &middot; ${esc(f.severity)}</div>
        <div>${esc(f.message)}</div>
        ${f.detail?.source_url ? `<div class="mt-1 small"><a href="${esc(f.detail.source_url)}" target="_blank" rel="noopener">View clause source ↗</a></div>` : ''}
      </div>
    </div>`).join('');
}

function renderCerts(certs, summary) {
  if (!certs?.schemes?.length) {
    E.certList.innerHTML = `<p class="text-muted small">${esc(certs?.note || 'No certification rule curated for this family yet.')}</p>`; return;
  }
  const tDate = summary.tender_date, dDate = summary.delivery_date;
  E.certList.innerHTML = certs.schemes.map(s => {
    const hist = s.order_history;
    const allDates = [...hist.map(h => h.effective_date), tDate, dDate].filter(Boolean).sort();
    const min = allDates[0], max = allDates[allDates.length - 1];
    const pct = d => {
      if (!d || min === max) return 50;
      const r = (new Date(d) - new Date(min)) / (new Date(max) - new Date(min));
      return 5 + r * 90;
    };
    let dots = '';
    hist.forEach(h => {
      if (!h.effective_date) return;
      dots += `<div class="tl-dot tl-dot-order" style="left:${pct(h.effective_date)}%" title="${esc(h.order_ref)}: ${esc(h.effective_date)}"></div>`;
    });
    if (tDate) { const p = pct(tDate); dots += `<div class="tl-dot tl-dot-tender" style="left:${p}%" title="Tender: ${tDate}"></div><div class="tl-label" style="left:${p}%">Tender</div>`; }
    if (dDate) { const p = pct(dDate); dots += `<div class="tl-dot tl-dot-delivery" style="left:${p}%" title="Delivery: ${dDate}"></div><div class="tl-label" style="left:${p}%">Delivery</div>`; }
    const histRows = hist.map(h => `<tr>
      <td class="font-mono">${esc(h.is_number)}</td>
      <td>${h.effective_date || (h.since_year ? `~${h.since_year}` : '<em>unconfirmed</em>')}</td>
      <td>${esc(h.enterprise_size)}</td>
      <td><span class="badge bg-secondary">${esc(h.state)}</span></td>
      <td>${h.source_url ? `<a href="${esc(h.source_url)}" target="_blank" rel="noopener">src ↗</a>` : '—'}</td>
    </tr>`).join('');
    return `
    <div class="cert-card">
      <div class="d-flex justify-content-between align-items-start flex-wrap gap-2 mb-1">
        <div class="fw-bold">${esc(s.scheme_label || s.scheme)}</div>
        <span class="verdict-pill vp-${s.verdict}">${VERDICT_LABELS[s.verdict] || s.verdict}</span>
      </div>
      <div class="small text-muted">${esc(s.controlling_order.order_ref)}${s.controlling_order.effective_date ? ' · effective ' + s.controlling_order.effective_date : ''}</div>
      ${s.controlling_order.notes ? `<div class="small mt-1">${esc(s.controlling_order.notes)}</div>` : ''}
      ${s.caveat ? `<div class="caveat-box mt-2"><i class="bi bi-exclamation-triangle-fill me-1"></i>${esc(s.caveat)}</div>` : ''}
      <div class="timeline-wrap"><div class="tl-track"></div>${dots}</div>
      <details class="mt-2">
        <summary class="small text-primary" style="cursor:pointer;">Full order history (${hist.length} entries)</summary>
        <div class="table-responsive mt-2">
          <table class="table table-sm hist-table mb-0">
            <thead><tr><th>IS number</th><th>Effective</th><th>Size</th><th>State</th><th></th></tr></thead>
            <tbody>${histRows}</tbody>
          </table>
        </div>
      </details>
    </div>`;
  }).join('');
}

function renderUnderstood(data) {
  const params = (data.extracted_params || []).map(p =>
    `<span class="param-chip">${esc(p.name.replace(/_/g,' '))}: ${p.value} ${esc(p.unit)}</span>`
  ).join('') || '<span class="text-muted">none detected</span>';
  const cited = (data.cited_standards || []).map(c =>
    `<span class="cited-chip">${esc(c.is_number)}${c.year ? ':'+c.year : ''}</span>`
  ).join('') || '<span class="text-muted">none detected</span>';
  const langLabels = { en: 'English', hi: 'Hindi', ta: 'Tamil', te: 'Telugu', kn: 'Kannada', gu: 'Gujarati', mr: 'Marathi' };
  const langDisplay = langLabels[data.family_detection.detected_language] || data.family_detection.detected_language || 'English';
  const conf = data.family_detection.confidence_band;
  const confColor = conf === 'high' ? 'text-success' : conf === 'medium' ? 'text-warning' : 'text-danger';
  E.understoodPanel.innerHTML = `
    <div class="understood-panel">
      <dl class="mb-0">
        <dt>Product family</dt>
        <dd>${esc(data.family_detection.detected_family_name || 'Not determined')} <span class="${confColor} small">(${conf || 'none'})</span></dd>
        <dt>Input language</dt>
        <dd>${esc(langDisplay)}${data.family_detection.was_expanded ? ' <span class="badge bg-info text-dark" style="font-size:.65rem;">trade/regional terms expanded</span>' : ''}</dd>
        <dt>Grade detected</dt>
        <dd>${esc(data.extracted_grade || 'None')}</dd>
        <dt>Parameters detected</dt>
        <dd>${params}</dd>
        <dt>IS numbers cited in text</dt>
        <dd>${cited}</dd>
        <dt>Dates / enterprise</dt>
        <dd>${esc(data.input_summary.tender_date)} → ${esc(data.input_summary.delivery_date || 'not specified')} · ${esc(data.input_summary.enterprise_size)}</dd>
      </dl>
    </div>`;
}

function renderClause(data) {
  const primary = (data.recommendations || []).filter(r => r.role === 'primary');
  const allied = (data.recommendations || []).filter(r => r.role !== 'primary' && r.mandatory);
  const lines = [];
  if (data.family_detection.abstained || !primary.length) {
    lines.push('// No confident recommendation — add more specification detail before drafting a clause.');
  } else {
    primary.forEach(p => lines.push(`Material/product shall conform to ${p.display_number}: ${p.title}.`));
    lines.push('');
    if (allied.length) {
      lines.push('Mandatory allied standards:');
      allied.forEach(a => {
        const role = (ROLE_LABELS[a.role] || a.role).toLowerCase();
        lines.push(`  - ${a.display_number} (${role})${a.condition ? ' [when: ' + a.condition + ']' : ''}: ${a.title}.`);
      });
      lines.push('');
    }
    (data.certifications?.schemes || []).forEach(s => {
      lines.push(`Certification (${s.scheme}): ${VERDICT_LABELS[s.verdict] || s.verdict}`);
      lines.push(`  Order: ${s.controlling_order.order_ref}${s.controlling_order.effective_date ? ', effective ' + s.controlling_order.effective_date : ''}.`);
      if (s.caveat) lines.push(`  NOTE: ${s.caveat}`);
      lines.push('');
    });
    const highFindings = (data.findings || []).filter(f => f.severity === 'high');
    if (highFindings.length) {
      lines.push('// REVIEW BEFORE FINALISING — High-severity issues found:');
      highFindings.forEach(f => lines.push(`// [${f.type.replace(/_/g,' ')}] ${f.message}`));
      lines.push('');
    }
  }
  lines.push(`// Generated by BIS Standards Recommender — data as of ${data.data_as_of}`);
  lines.push('// Decision-support only. Verify on BIS Manak portal before use in a tender.');
  E.clauseBox.value = lines.join('\n');
}
