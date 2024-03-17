import API from "../API";
import CharacteristicBO from "../CharacteristicBO";
export default class CharacteristicView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new CharacteristicView();
    }
    return this.#view;
  }
  #getByidURL = (id) => `characteristic/${id}`;
  #getAllStandartURL = () => `default-characteristic`;
  #getAllURL = () => `characteristic`;
  #createURL = () => `characteristic`;
  #updateURL = (id) => `characteristic/${id}`;
  #deleteURL = (id) => `characteristic/${id}`;

  getById(id) {
    return API.getAPI().get(this.#getByidURL(id), CharacteristicBO);
  }

  getAllStandart() {
    return API.getAPI().get(this.#getAllStandartURL(), CharacteristicBO);
  }
  getAll() {
    return API.getAPI().get(this.#getAllURL(), CharacteristicBO);
  }

  create(characteristic) {
    return API.getAPI().create(
      this.#createURL(),
      characteristic,
      CharacteristicBO
    );
  }

  update(characteristic) {
    return API.getAPI().update(
      this.#updateURL(characteristic.getID()),
      characteristic,
      CharacteristicBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), CharacteristicBO);
  }
}
