function toggleSpoiler(id, state = undefined) {
  const spoiler = document.querySelector(`.spoiler[data-spoiler-id='${id}']`);
  if (!spoiler) {
    console.warn(`Spoiler with id ${id} is not found`);
    return;
  }
  spoiler.classList.toggle("spoiler-opened", state);
}

function copyableCopy(id) {
  const copyable = document.querySelector(
    `.copyable[data-copyable-id='${id}'] .copyable__content`
  );
  if (!copyable) {
    console.warn(`Copyable with id ${id} is not found`);
    return;
  }
  navigator.clipboard.writeText(copyable.textContent);
}

function autocompleteTagsUpdateList(id) {
  const chipContainer = document.querySelector(
    `.input-tag#${id} .input-tag__tags`
  );
  chipContainer.innerHTML = "";

  const tags = autocompleteValues[id];
  let index = 0;
  tags.forEach((tag) => {
    const li = document.createElement("li");
    li.innerHTML = `
    <div class="chip">
      ${tag}
      <a href="#" onclick="autocompleteTagsRemove('${id}', '${tag}')">&#10006;</a>
    </div>
    <input type="hidden" name="tags-${index++}" value="${tag}"/>
    `;
    chipContainer.appendChild(li);
  });
}

function autocompleteTagsAdd(id) {
  const input = document.querySelector(`.input-tag#${id} .input`);
  if (!input) {
    console.warn(`Input with id ${id} is not found`);
    return;
  }
  const value = input.value;
  if (!value) return;
  input.value = "";

  autocompleteAddValue(id, value);
  autocompleteTagsUpdateList(id);
}

function autocompleteTagsRemove(id, value) {
  autocompleteRemoveValue(id, value);
  autocompleteTagsUpdateList(id);
}
