import BusinessObject from "./BusinessObject";

/**
 * Represents a SearchProfile
 */
export default class SearchProfileBO extends BusinessObject {
  /**
   * Constructs a SearchProfileBO object with a given UserProfile ID.
   *
   * @param {String} aUserProfileId -Attribut of SearchProfileBO.

   */
  constructor(aUserProfileId) {
    super();
    this.userprofile_id = aUserProfileId;
  }

  /**
   * Sets a new UserProfile ID.
   *
   * @param {String} aUserProfileId - the new UserProfile of this SearchProfileBO.
   */
  setUserProfileId(aUserProfileId) {
    this.userprofile_id = aUserProfileId;
  }

  /**
   * Gets the Userprofile_id.
   */
  getUserProfileId() {
    return this.userprofile_id;
  }

  /**
   * Returns an Array of SearchProfileBOs from a given JSON structure.
   */
  static fromJSON(searchProfiles) {
    let result = [];

    if (Array.isArray(searchProfiles)) {
      searchProfiles.forEach((u) => {
        Object.setPrototypeOf(u, SearchProfileBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = searchProfiles;
      Object.setPrototypeOf(u, SearchProfileBO.prototype);
      result.push(u);
    }

    return result;
  }
}
