function toggleSpoiler(id, state = undefined) {
  const spoiler = document.querySelector(`.spoiler[data-spoiler-id='${id}']`);
  if (!spoiler) {
    console.warn(`Spoiler with id ${id} is not found`);
    return;
  }
  spoiler.classList.toggle("spoiler-opened", state);
}
