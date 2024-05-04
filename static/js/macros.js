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
