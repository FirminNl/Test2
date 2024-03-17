import API from "../API";
import UserProfileBO from "../UserProfileBO";
export default class UserProfileView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new UserProfileView();
    }
    return this.#view;
  }
  #getByGuidURL = (guid) => `user-by-guid/${guid}`;
  #createURL = () => `user`;
  #updateURL = (id) => `user/${id}`;
  #deleteURL = (id) => `user/${id}`;
  #getByIdURL = (id) => `user/${id}`;

  getByGuid(guid) {
    return API.getAPI().get(this.#getByGuidURL(guid), UserProfileBO);
  }

  getById(guid) {
    return API.getAPI().get(this.#getByIdURL(guid), UserProfileBO);
  }

  create(userProfile) {
    return API.getAPI().create(this.#createURL(), userProfile, UserProfileBO);
  }

  update(userProfile) {
    return API.getAPI().update(
      this.#updateURL(userProfile.getID()),
      userProfile,
      UserProfileBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), UserProfileBO);
  }
}