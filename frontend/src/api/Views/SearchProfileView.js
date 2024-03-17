import API from "../API";
import SearchProfileBO from "../SearchProfileBO";
export default class SearchProfileView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new SearchProfileView();
    }
    return this.#view;
  }
  #getByUserprofileIdURL = (userprofile_id) =>
    `searchprofile/${userprofile_id}`;
  #createURL = () => `searchprofile`;
  #updateURL = (id) => `searchprofile/${id}`;
  #deleteURL = (id) => `searchprofile/${id}`;

  getByUserprofileId(userprofile_id) {
    return API.getAPI().get(
      this.#getByUserprofileIdURL(userprofile_id),
      SearchProfileBO
    );
  }

  create(searchProfile) {
    return API.getAPI().create(
      this.#createURL(),
      searchProfile,
      SearchProfileBO
    );
  }

  update(searchProfile) {
    return API.getAPI().update(
      this.#updateURL(searchProfile.getID()),
      searchProfile,
      SearchProfileBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), SearchProfileBO);
  }
}