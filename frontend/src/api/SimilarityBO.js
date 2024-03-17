import BusinessObject from "./BusinessObject";

/**
 * Represents a Similarity
 */
export default class SimilarityBO extends BusinessObject {
  /**
   * Constructs a SimilarityBO object with a given matching ID, score ID.
   * @param {String} aMatchingId -Attribut of SimilarityBO.
   * @param {String} aScore -Attribut of SimilarityBO.
   */
  constructor(aMatchingId, aScore) {
    super();
    this.matching_id = aMatchingId;
    this.score = aScore;
  }

  /**
   * Sets matching ID.
   *
   * @param {String} aMatchingId - the new matching ID of this SimilarityBO.
   */
  setMatchingId(aMatchingId) {
    this.matching_id = aMatchingId;
  }

  /**
   * Gets the Userprofile ID.
   */
  getUserprofileId() {
    return this.userprofile_id;
  }

  /**
   * Sets a new score.
   *
   * @param {String} aScore - the score ID of this Similarity BO.
   */
  setScore(aScore) {
    this.score = aScore;
  }

  getScore() {
    return this.score;
  }

  /**
   * Returns an Array of SimilarityBOs from a given JSON structure.
   */
  static fromJSON(Similarities) {
    let result = [];

    if (Array.isArray(Similarities)) {
      Similarities.forEach((u) => {
        Object.setPrototypeOf(u, SimilarityBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Similarities;
      Object.setPrototypeOf(u, SimilarityBO.prototype);
      result.push(u);
    }

    return result;
  }
}
