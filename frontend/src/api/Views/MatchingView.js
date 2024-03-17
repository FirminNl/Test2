import API from "../API";
import MatchingBO from "../MatchingBO";
export default class MatchingView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new MatchingView();
    }
    return this.#view;
  }
  #getByUserProfileIdURL = (userprofile_id) => `matching/${userprofile_id}`;
  #createURL = () => `matching`;
  #updateURL = (id) => `matching/${id}`;
  #deleteURL = (id) => `matching/${id}`;

  getByUserProfileId(userprofile_id) {
    return API.getAPI().get(
      this.#getByUserProfileIdURL(userprofile_id),
      MatchingBO
    );
  }

  create(matching) {
    return API.getAPI().create(this.#createURL(), matching, MatchingBO);
  }

  update(matching) {
    return API.getAPI().update(
      this.#updateURL(matching.getID()),
      matching,
      MatchingBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), MatchingBO);
  }
}
