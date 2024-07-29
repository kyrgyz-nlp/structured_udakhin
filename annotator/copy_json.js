function copyJSON() {
  const jsonElement = document.querySelector('#json');
  if (jsonElement) {
    const textToCopy = jsonElement.textContent || jsonElement.innerText;
    navigator.clipboard.writeText(textToCopy)
      .then(() => {
        console.log('Text copied to clipboard');
      })
      .catch(err => {
        console.error('Failed to copy text: ', err);
      });
  } else {
    console.error('Element with id "json" not found');
  }
}
