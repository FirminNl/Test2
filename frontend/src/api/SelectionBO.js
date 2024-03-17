import BusinessObject from "./BusinessObject";

/**
 * Represents a Selection
 */
export default class SelectionBO extends BusinessObject {
  /**
   * Constructs a SelectionBO object with a characteristic ID characteristic_id, answer of description & max answer.
   *
   * @param {String} aCharacteristicId -Attribut of SelectionBO.
   * @param {String} aAnswer -Attribut of SelectionBO.
   */
  constructor(aCharacteristicId, aAnswer) {
    super();
    this.characteristic_id = aCharacteristicId;
    this.answer = aAnswer;
  }

  /**
   * Sets a new characteristic_id.
   *
   * @param {String} aCharacteristicId - the new characteristic_id of this SelectionBO.
   */
  setCharacteristicId(aCharacteristicId) {
    this.characteristic_id = aCharacteristicId;
  }

  /**
   * Gets the characteristic_id.
   */
  getCharacteristicId() {
    return this.characteristic_id;
  }

  /**
   * Sets a new aAnswer.
   *
   * @param {*} aAnswer - the new aAnswer of this SelectionBO.
   */
  setAnswer(aAnswer) {
    this.answer = aAnswer;
  }

  /**
   * Gets the Answer.
   */
  getAnswer() {
    return this.answer;
  }

  /**
   * Returns an Array of SelectionBOs from a given JSON structure.
   */
  static fromJSON(Selections) {
    let result = [];

    if (Array.isArray(Selections)) {
      Selections.forEach((u) => {
        Object.setPrototypeOf(u, SelectionBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Selections;
      Object.setPrototypeOf(u, SelectionBO.prototype);
      result.push(u);
    }

    return result;
  }
}

