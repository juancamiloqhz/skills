export function renderReport(rows) {
  return rows.map(row => formatRow(row));
}

export function formatRow(row) {
  return lookupLabel(row.id) + normalize(row.value);
}

export function normalize(value) {
  return String(value).trim();
}

export function lookupLabel(id) {
  return labels.find(row => row.id === id).label;
}

const labels = [{id: 1, label: "one"}];
