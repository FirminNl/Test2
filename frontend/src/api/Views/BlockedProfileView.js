import API from "../API";
import BlockedProfileBO from "../BlockedProfileBO";
export default class BlockedProfileView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new BlockedProfileView();
    }
    return this.#view;
  }
  #getByUserprofile_idURL = (userprofile_id) => `blockedprofile/${userprofile_id}`;
  #createURL = () => `blockedprofile`;
  #updateURL = (id) => `blockedprofile/${id}`;
  #deleteURL = (id) => `blockedprofile/${id}`;

  getByUserprofile_id(userprofile_id) {
    return API.getAPI().get(this.#getByUserprofile_idURL(userprofile_id), BlockedProfileBO);
  }

  create(blockedProfile) {
    return API.getAPI().create(this.#createURL(), blockedProfile, BlockedProfileBO);
  }

  update(blockedProfile) {
    return API.getAPI().update(
      this.#updateURL(blockedProfile.getID()),
      blockedProfile,
      BlockedProfileBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), BlockedProfileBO);
  }
}

