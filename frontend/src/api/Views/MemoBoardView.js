import API from "../API";
import MemoBoardBO from "../MemoBoardBO";
export default class MemoBoardView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new MemoBoardView();
    }
    return this.#view;
  }
  #getByUserprofile_idURL = (userprofile_id) => `memoboard/${userprofile_id}`;
  #createURL = () => `memoboard`;
  #updateURL = (id) => `memoboard/${id}`;
  #deleteURL = (id) => `memoboard/${id}`;

  getByUserprofile_id(userprofile_id) {
    return API.getAPI().get(this.#getByUserprofile_idURL(userprofile_id), MemoBoardBO);
  }

  create(memoBoard) {
    return API.getAPI().create(this.#createURL(), memoBoard, MemoBoardBO);
  }

  update(memoBoard) {
    return API.getAPI().update(
      this.#updateURL(memoBoard.getID()),
      memoBoard,
      MemoBoardBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), MemoBoardBO);
  }
}
