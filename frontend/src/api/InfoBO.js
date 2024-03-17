import BusinessObject from "./BusinessObject";

/**
 * Represents a Info
 */
export default class InfoBO extends BusinessObject {
  /**
   * Constructs a InfoBO object with a given Userprofile ID, Answer ID, Is Selection Info or Description, is Searchprofile or Profile Info.
   *
   * @param {String} aUserprofileId -Attribut of InfoBO.
   * @param {String} aIsSearchprofile -Attribut of InfoBO.
   * @param {boolean} aIsSelection -Attribut of InfoBO.
   * @param {boolean} aIsSearchprofile -Attribut of InfoBO.
   */

  constructor(aUserprofileId, aAnswerId, aIsSelection, aIsSearchprofile) {
    super();
    this.userprofile_id = aUserprofileId;
    this.answer_id = aAnswerId;
    this.is_selection = aIsSelection;
    this.is_searchprofile = aIsSearchprofile;
  }

  /**
   * Sets a Userprofile ID  of Info.
   *
   * @param {String} aUserprofileId - the new Userprofile ID of this InfoBO.
   */
  setUserprofileId(aUserprofileId) {
    this.userprofile_id = aUserprofileId;
  }

  /**
   * Gets the Userprofile ID of InfoBO.
   */
  getUserprofileId() {
    return this.userprofile_id;
  }
  getAnswerId() {
    return this.answer_id;
  }

  /**
   * Sets a new Answer Id.
   *
   * @param {String} aIsSearchprofile - the new Answer ID of InfoBO.
   */
  setAnswerId(aAnswerId) {
    this.answer_id = aAnswerId;
  }

  /**
   * Sets a new Is Selection.
   * @param {Boolean} aIsSelection - the new Is Selection as boolean for InfoBO.
   */
  setIsSelection(aIsSelection) {
    this.is_selection = aIsSelection;
  }

  /**
   * Gets the Is Selection as boolean value for InfoBO.
   */
  getIsSelection() {
    return this.is_selection;
  }

  setIsSearchprofile(aIsSearchprofile) {
    this.is_searchprofile = aIsSearchprofile;
  }

  /**
   * Gets the boolean value of is Searchprofile.
   */
  getIsSearchprofile() {
    return this.is_searchprofile;
  }

  /**
   * Returns an Array of InfoBOs from a given JSON structure.
   */
  static fromJSON(Infos) {
    let result = [];

    if (Array.isArray(Infos)) {
      Infos.forEach((u) => {
        Object.setPrototypeOf(u, InfoBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Infos;
      Object.setPrototypeOf(u, InfoBO.prototype);
      result.push(u);
    }

    return result;
  }
}