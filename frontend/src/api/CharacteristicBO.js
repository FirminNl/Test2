import BusinessObject from "./BusinessObject";

/**
 * Represents a Characteristic
 */
export default class CharacteristicBO extends BusinessObject {
  /**
   * Constructs a CharacteristicBO object with a given name and standard .
   *
   * @param {String} aName -Attribut of CharacteristicBO.
   * @param {boolean} aStandart -Attribut of CharacteristicBO.
   * @param {boolean} aIs_selection -Attribut of CharacteristicBO.
   * @param {Integer} aAuthor_id -Attribut of CharacteristicBO.
   */
  constructor(aName, aIsStandart, aIsSelection, aAuthor_id, aDescription) {
    super();
    this.name = aName;
    this.is_standart = aIsStandart;
    this.is_selection = aIsSelection;
    this.author_id = aAuthor_id;
    this.description = aDescription;
  }

  /**
   * Sets a new name.
   *
   * @param {String} aName - the new name of this CharacteristicBO.
   */
  setName(aName) {
    this.name = aName;
  }

  /**
   * Gets the name.
   */
  getName() {
    return this.name;
  }

  /**
   * Sets a new Standart boolean value.
   *
   * @param {boolean} aIsStandart - the new Standart boolean value of this CharacteristicBO.
   */
  setIsStandart(aIsStandart) {
    this.is_standart = aIsStandart;
  }

  /**
   * Gets the Standart.
   */
  getIsStandart() {
    return this.is_standart;
  }

  /**
   * Sets a new is Selection boolean value.
   *
   * @param {boolean} aIsSelection - the new Is Selection boolean value of this CharacteristicBO.
   */
  setIsSelection(aIsSelection) {
    this.is_selection = aIsSelection;
  }

  /**
   * Gets the Standart.
   */
  getIsSelection() {
    return this.is_selection;
  }

  /**
   * Sets a new is Author ID Integer value.
   *
   * @param {Integer} author ID - the new Author ID Integer value of this CharacteristicBO.
   */
  setAuthorId(aAuthor_id) {
    this.author_id = aAuthor_id;
  }

  /**
   * Gets the Author ID.
   */
  getAuthorId() {
    return this.author_id;
  }

  setDescription(aDescription) {
    this.description = aDescription;
  }

  /**
   * Gets the Author ID.
   */
  getDescription() {
    return this.description;
  }

  /**
   * Returns an Array of CharacteristicBOs from a given JSON structure.
   */
  static fromJSON(Characteristics) {
    let result = [];

    if (Array.isArray(Characteristics)) {
      Characteristics.forEach((u) => {
        Object.setPrototypeOf(u, CharacteristicBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Characteristics;
      Object.setPrototypeOf(u, CharacteristicBO.prototype);
      result.push(u);
    }

    return result;
  }
}
