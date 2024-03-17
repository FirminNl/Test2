import API from "../API";
import SimilarityBO from "../SimilarityBO";
export default class SimilarityView {
  static #view = null;
  static getView() {
    if (this.#view == null) {
      this.#view = new SimilarityView();
    }
    return this.#view;
  }
  #getByMatching_idURL = (matching_id) => `similarity/${matching_id}`;
  #createURL = () => `similarity`;
  #updateURL = (id) => `similarity/${id}`;
  #deleteURL = (id) => `similarity/${id}`;

  getByMatching_id(matching_id) {
    return API.getAPI().get(this.#getByMatching_idURL(matching_id), SimilarityBO);
  }

  create(similarity) {
    return API.getAPI().create(this.#createURL(), similarity, SimilarityBO);
  }

  update(similarity) {
    return API.getAPI().update(
      this.#updateURL(similarity.getID()),
      similarity,
      SimilarityBO
    );
  }

  delete(id) {
    return API.getAPI().delete(this.#deleteURL(id), SimilarityBO);
  }
}

