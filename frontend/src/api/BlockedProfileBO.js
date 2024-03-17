import BusinessObject from "./BusinessObject";

/**
 * Represents a UserProfile
 */
export default class BlockedProfileBO extends BusinessObject {
  /**
   * Constructs a BlockedProfileBO object with a given Userprofile ID & Blockeduser ID.
   *
   * @param {String} aUserprofileId -Attribut of BlockedProfileBO.
   * @param {String} aBlockedUserId -Attribut of BlockedProfileBO.
   
   */
  constructor(aUserprofileId, aBlockedUserId) {
    super();
    this.userprofile_id = aUserprofileId;
    this.blockeduser_id = aBlockedUserId;
  }

  /**
   * Sets a new userprofile_id.
   *
   * @param {String} aUserprofileId - the new userprofile_id of this BlockedProfileBO.
   */
  setUserprofileId(aUserprofileId) {
    this.userprofile_id = aUserprofileId;
  }

  /**
   * Gets the userprofile ID.
   */
  getUserprofileId() {
    return this.userprofile_id;
  }

  /**
   * Sets a new Blocked User Id.
   *
   * @param {*} aBlockedUserId - the new Blocked User Id of this BlockedProfileBO.
   */
  setBlockeduserId(aBlockedUserId) {
    this.blockeduser_id = aBlockedUserId;
  }

  /**
   * Gets the Surname.
   */
  getBlockeduserId() {
    return this.blockeduser_id;
  }

  /**
   * Returns an Array of BlockedProfileBOs from a given JSON structure.
   */
  static fromJSON(blockedProfiles) {
    let result = [];

    if (Array.isArray(blockedProfiles)) {
      blockedProfiles.forEach((u) => {
        Object.setPrototypeOf(u, BlockedProfileBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = blockedProfiles;
      Object.setPrototypeOf(u, BlockedProfileBO.prototype);
      result.push(u);
    }

    return result;
  }
}
