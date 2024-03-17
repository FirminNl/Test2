import BusinessObject from "./BusinessObject";

/**
 * Represents a Info
 */
export default class MatchingBO extends BusinessObject {
  /**
   * Constructs a InfoBO object with a given Matching ID, Userprofile ID, Candidateprofile ID, unseen profile or seen profile
   *
   * @param {String} aUserprofileId -Attribut of MatchingBO.
   * @param {String} aCandidateprofileId -Attribut of MatchingBO.
   * @param {boolean} aUnseenProfile -Attribut of MatchingBO.
   y
   */
  constructor(aUserprofileId, aCandidateprofileId, aUnseenProfile) {
    super();
    this.userprofile_id = aUserprofileId;
    this.candidateprofile_id = aCandidateprofileId;
    this.unseen_profile = aUnseenProfile;
  }

  /**
   * Sets userprofile ID.
   *
   * @param {String} aUserprofileId - the new Userprofile ID of this MatchingBO.
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
   * Sets a new candidateprofile Id.
   *
   * @param {String} aCandidateprofileId - the new Candidateprofile ID of this Matching BO.
   */
  setCandidateprofileId(aCandidateprofileId) {
    this.candidateprofile_id = aCandidateprofileId;
  }

  /**
   * Gets the Userprofile ID.
   */
  getCandidateprofileId() {
    return this.candidateprofile_id;
  }

  /**
   * Sets unseenprofile with TRUE(matching) or False(profile).
   * @param {Boolean} aUnseenProfile - the new Answer ID of this InfoBO.
   */
  setUnseenProfile(aUnseenProfile) {
    this.unseen_profile = aUnseenProfile;
  }

  /**
   * Gets the Is Selection boolean value.
   */
  getUnseenProfile() {
    return this.unseen_profile;
  }



  /**
   * Returns an Array of InfoBOs from a given JSON structure.
   */
  static fromJSON(Matchings) {
    let result = [];

    if (Array.isArray(Matchings)) {
      Matchings.forEach((u) => {
        Object.setPrototypeOf(u, MatchingBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Matchings;
      Object.setPrototypeOf(u, MatchingBO.prototype);
      result.push(u);
    }

    return result;
  }
}

