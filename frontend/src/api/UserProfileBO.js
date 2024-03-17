import BusinessObject from "./BusinessObject";

/**
 * Represents a UserProfile
 */
export default class UserProfileBO extends BusinessObject {
  /**
   * Constructs a UserProfileBO object with a given firstname and surname.
   *
   * @param {String} aFirstname -Attribut of UserProfileBO.
   * @param {String} aSurname -Attribut of UserProfileBO.
   * @param {String} aEmail -Attribut of UserProfileBO.
   * @param {String} aGoogleUserId -Attribut of UserProfileBO.
   * @param {String} aAboutMe -Attribut of UserProfileBO.
   */
  constructor(aGoogleUserId, aEmail, aFirstname, aSurname, aAboutMe) {
    super();
    this.google_user_id = aGoogleUserId;
    this.email = aEmail;
    this.firstname = aFirstname;
    this.surname = aSurname;
    this.about_me = aAboutMe;
  }

  /**
   * Sets a new firstname.
   *
   * @param {String} aFirstname - the new firstname of this UserProfileBO.
   */
  setFirstname(aFirstname) {
    this.firstname = aFirstname;
  }

  /**
   * Gets the firstname.
   */
  getFirstname() {
    return this.firstname;
  }

  /**
   * Sets a new surname.
   *
   * @param {*} aSurname - the new surname of this UserProfileBO.
   */
  setSurname(aSurname) {
    this.surname = aSurname;
  }

  /**
   * Gets the Surname.
   */
  getSurname() {
    return this.surname;
  }

  setAboutMe(aAboutMe) {
    this.about_me = aAboutMe;
  }

  /**
   * Gets the About Me.
   */
  getAboutMe() {
    return this.about_me;
  }

  setEmail(aEmail) {
    this.email = aEmail;
  }

  getEmail() {
    return this.email;
  }

  setGoogleUserId(aGoogleUserId) {
    this.google_user_id = aGoogleUserId;
  }

  getGoogleUserId() {
    return this.google_user_id;
  }

  /**
   * Returns an Array of UserProfileBOs from a given JSON structure.
   */
  static fromJSON(userProfiles) {
    let result = [];

    if (Array.isArray(userProfiles)) {
      userProfiles.forEach((u) => {
        Object.setPrototypeOf(u, UserProfileBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = userProfiles;
      Object.setPrototypeOf(u, UserProfileBO.prototype);
      result.push(u);
    }

    return result;
  }
}