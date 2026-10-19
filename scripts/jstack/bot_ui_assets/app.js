const sendButton = document.getElementById('send');
const refreshButton = document.getElementById('refresh');
const newButton = document.getElementById('new');
const statusText = document.getElementById('status');
let storageKey;
let requestId;

function show(state) {
  const outcome = state.delivery.outcome;
  if (state.processing === 'completed') {
    statusText.textContent = 'Check recorded as complete. If the conversation result is missing, ask to recover the saved result using this request ID.';
  } else if (state.processing === 'acknowledged_without_result') {
    statusText.textContent = 'An earlier receiver recorded completion without saving the result. Ask to reconcile this request; do not resend.';
  } else if (state.processing === 'result_saved') {
    statusText.textContent = 'PR result saved. Delivery to the conversation is not yet acknowledged.';
  } else if (state.processing === 'claimed') {
    statusText.textContent = 'A receiver has claimed this check. Completion is not yet recorded.';
  } else if (outcome === 'accepted' || outcome === 'duplicate') {
    statusText.textContent = 'Delivery accepted. The check is not yet confirmed complete.';
  } else if (outcome === 'recorded') {
    statusText.textContent = 'T3 recorded the delivery, but did not return its outcome. The check may not have started. Refresh status; do not resend.';
  } else if (outcome === 'queued') {
    statusText.textContent = 'T3 queued the request for delivery when the environment is available. The check is not yet confirmed started. Do not resend.';
  } else {
    statusText.textContent = `Delivery ${outcome}. The request is saved for receiver recovery. No automatic resend.`;
  }
  sendButton.disabled = true;
  newButton.disabled = state.processing !== 'completed';
}

async function refresh() {
  const response = await fetch(`/requests/${requestId}`);
  if (response.status === 404) {
    statusText.textContent = 'This request is not recorded. Click Check PR to submit it.';
    sendButton.disabled = false;
    newButton.disabled = true;
  } else if (response.ok) {
    show(await response.json());
  } else {
    throw new Error('status unavailable');
  }
}

function selectRequest() {
  requestId = localStorage.getItem(storageKey);
  if (!requestId) {
    requestId = Array.from(crypto.getRandomValues(new Uint8Array(16)), byte => byte.toString(16).padStart(2, '0')).join('');
    localStorage.setItem(storageKey, requestId);
  }
  if (!/^[A-Za-z0-9_-]{1,80}$/.test(requestId)) throw new Error('invalid saved request ID');
  document.getElementById('request').textContent = `Request: ${requestId}`;
}

function uncertain() {
  statusText.textContent = 'Cannot confirm status. Keep this request ID and refresh status before taking another action.';
  sendButton.disabled = true;
  newButton.disabled = true;
}

sendButton.addEventListener('click', async () => {
  sendButton.disabled = true;
  statusText.textContent = 'Submitting this request…';
  try {
    const response = await fetch('/requests', {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({requestId}),
    });
    if (!response.ok) throw new Error('submission unconfirmed');
    show(await response.json());
  } catch { uncertain(); }
});
refreshButton.addEventListener('click', () => refresh().catch(uncertain));
newButton.addEventListener('click', async () => {
  newButton.disabled = true;
  try {
    localStorage.removeItem(storageKey);
    selectRequest();
    await refresh();
  } catch { uncertain(); }
});

(async () => {
  try {
    const response = await fetch('/scope');
    if (!response.ok) throw new Error('scope unavailable');
    const scope = await response.json();
    document.getElementById('scope').textContent = `${scope.repository} · PR #${scope.pr}`;
    storageKey = `jstack-check:${scope.repository}:${scope.pr}`;
    selectRequest();
    refreshButton.disabled = false;
    await refresh();
  } catch {
    uncertain();
  }
})();
