function copyItem(selector) {
  const jsonElement = document.querySelector(selector);
  if (jsonElement) {
    const textToCopy = jsonElement.textContent || jsonElement.innerText;
    navigator.clipboard.writeText(textToCopy)
      .then(() => {
        console.log('Copied to clipboard');
      })
      .catch(err => {
        console.error('Failed to copy: ', err);
      });
  } else {
    console.error('Element with ' + selector + ' not found');
  }
}

function copyText() {
  copyItem('#text')
}

function copyAnnotation() {
  copyItem('#annotation')
}

function copyJSON() {
  copyItem('#json')
}
