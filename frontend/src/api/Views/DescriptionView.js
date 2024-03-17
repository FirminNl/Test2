import API from "../API";
import DescriptionBO from "../DescriptionBO";
export default class DescriptionView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new DescriptionView();
    }
    return this.#view;
  }
  #getByCharacteristicURL = (characteristic_id) =>
    `description-by-char/${characteristic_id}`;
  #getByIdURL = (id) => `description/${id}`;
  #createURL = () => `description`;
  #updateURL = (id) => `description/${id}`;
  #deleteURL = (id) => `description/${id}`;

  getByCharacteristic(characteristic_id) {
    return API.getAPI().get(
      this.#getByCharacteristicURL(characteristic_id),
      DescriptionBO
    );
  }

  getById(id) {
    return API.getAPI().get(this.#getByIdURL(id), DescriptionBO);
  }

  create(description) {
    return API.getAPI().create(this.#createURL(), description, DescriptionBO);
  }

  update(description) {
    return API.getAPI().update(
      this.#updateURL(description.getID()),
      description,
      DescriptionBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), DescriptionBO);
  }
}
