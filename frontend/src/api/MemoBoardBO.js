import BusinessObject from "./BusinessObject";

/**
 * Represents a MemoBoard
 */
export default class MemoBoardBO extends BusinessObject {
  /**
   * Constructs a MemoBoardBO object with a given Userprofile ID, Matching ID, saved ID  .
   *
   * @param {String} aUserprofileId -Attribut of MemoBoardBO.
   * @param {String} aSavedId -Attribut of MemoBoardBO.
   */
  constructor(aUserprofileId, aSavedId) {
    super();
    this.userprofile_id = aUserprofileId;
    this.saved_id = aSavedId;
  }

  /**
   * Sets a Userprofile ID  of MemoBoard.
   *
   * @param {String} aUserprofileId - the new Userprofile ID of this MemoBoardBO.
   */
  setUserprofileId(aUserprofileId) {
    this.userprofile_id = aUserprofileId;
  }

  /**
   * Gets the Userprofile ID.
   */
  getUserprofileId() {
    return this.userprofile_id;
  }

  /**
   * Sets a new saved ID.
   * @param {String} aSavedId - the new is Saved ID of MemoBoardBO.
   */
  setSavedId(aSavedId) {
    this.saved_id = aSavedId;
  }

  /**
   * Gets saved Id of MemoBoard.
   */
  getSavedId() {
    return this.saved_id;
  }

  /**
   * Returns an Array of MemoBoardBOs from a given JSON structure.
   */
  static fromJSON(MemoBoards) {
    let result = [];

    if (Array.isArray(MemoBoards)) {
      MemoBoards.forEach((u) => {
        Object.setPrototypeOf(u, MemoBoardBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = MemoBoards;
      Object.setPrototypeOf(u, MemoBoardBO.prototype);
      result.push(u);
    }

    return result;
  }
}
