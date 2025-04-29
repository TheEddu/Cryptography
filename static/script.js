document.getElementById('cipherForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const text = document.getElementById('text').value;
    const shift = parseInt(document.getElementById('shift').value);
    const direction = document.getElementById('direction').value;

    const response = await fetch('/cipher', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, shift, direction })
    });

    const data = await response.json();
    document.getElementById('result').innerText = 'Result: ' + data.result;
  });