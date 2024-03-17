import API from "../API";
import SelectionBO from "../SelectionBO";
export default class SelectionView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new SelectionView();
    }
    return this.#view;
  }
  #getByCharacteristicURL = (characteristicID) =>
    `selection-by-char/${characteristicID}`;
  #createURL = () => `selection`;
  #getByIdURL = (id) => `selection/${id}`;
  #updateURL = (id) => `selection/${id}`;
  #deleteURL = (id) => `selection/${id}`;

  getByCharacteristic(characteristicID) {
    return API.getAPI().get(
      this.#getByCharacteristicURL(characteristicID),
      SelectionBO
    );
  }

  getById(id) {
    return API.getAPI().get(this.#getByIdURL(id), SelectionBO);
  }

  create(selection) {
    return API.getAPI().create(this.#createURL(), selection, SelectionBO);
  }

  update(selection) {
    return API.getAPI().update(
      this.#updateURL(selection.getID()),
      selection,
      SelectionBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), SelectionBO);
  }
}

