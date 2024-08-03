const buildPrompt = (arg1, arg2, arg3) => {
  return `Сен сөздүк макалаларын туура форматка келтиргенге жардам берген досумсуң. Сен сөздүк макаласын алып, аннотатор көрсөткөн катаны эске алып, туура эмес болуп калган JSON структураны берилген JSON схеманы үлгү катары колдонуп, туураланган JSON структура бересиң.

Сөздүк макаласы:
${arg1}

Аннотация:
${arg2}

Туура эмес болуп калган JSON структурасы:
${arg3}

Төмөнкү JSON схемасы колдонулушу керек:
{
  "type": "object",
  "properties": {
    "ru": {
      "type": "string"
    },
    "meta": {
      "type": "string"
    },
    "ky": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "description": {
            "type": "object",
            "properties": {
              "ky": {
                "type": "string"
              },
              "ru": {
                "type": "string"
              }
            },
            "required": ["ky", "ru"]
          },
          "translations": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "examples": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "ru": {
                  "type": "string"
                },
                "ky": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "required": ["ru", "ky"]
            }
          }
        },
        "required": ["description", "translations", "examples"]
      }
    },
    "ref": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "word": {
            "type": "string"
          },
          "description": {
            "type": "object",
            "properties": {
              "ky": {
                "type": "string"
              },
              "ru": {
                "type": "string"
              }
            },
            "required": ["ky", "ru"]
          }
        },
        "required": ["word", "description"]
      }
    }
  },
  "required": ["ru", "meta", "ky"]
}

Туураланган структура:

`
}

function getItemText(selector) {
  const elementToCopy = document.querySelector(selector);
  if (elementToCopy) {
    return elementToCopy.textContent || elementToCopy.innerText;
  }
}

function copyAllItems() {
  const text = getItemText('#text')
  const annotation = getItemText('#annotation')
  const json = getItemText('#json')
  const prompt = buildPrompt(text, annotation, json)
  navigator.clipboard.writeText(prompt)
    .then(() => {
      console.log('Copied to clipboard');
    })
    .catch(err => {
      console.error('Failed to copy: ', err);
    });
}
