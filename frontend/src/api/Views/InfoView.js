import API from "../API";
import InfoBO from "../InfoBO";
import UserProfileBO from "../UserProfileBO";

export default class InfoView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new InfoView();
    }
    return this.#view;
  }
  #getByUserprofile_idURL = (userprofile_id) =>
    `info-userprofile/${userprofile_id}`;
  #getBySearchprofile_idURL = (searchprofile_id) =>
    `info-searchprofile/${searchprofile_id}`;
  #createURL = () => `info`;
  #updateURL = (id) => `info/${id}`;
  #deleteURL = (id) => `info/${id}`;

  getByUserprofile_id(userprofile_id) {
    return API.getAPI().get(
      this.#getByUserprofile_idURL(userprofile_id),
      InfoBO
    );
  }

  getBySearchprofile_id(searchprofile_id) {
    return API.getAPI().get(
      this.#getBySearchprofile_idURL(searchprofile_id),
      InfoBO
    );
  }

  create(info) {
    return API.getAPI().create(this.#createURL(), info, InfoBO);
  }

  update(info) {
    return API.getAPI().update(this.#updateURL(info.getID()), info, InfoBO);
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), InfoBO);
  }
}
