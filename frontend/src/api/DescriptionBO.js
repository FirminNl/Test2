import BusinessObject from "./BusinessObject";

/**
 * Represents a Description
 */
export default class DescriptionBO extends BusinessObject {
  /**
   * Constructs a DescriptionBO object with a characteristic ID characteristic_id, answer of description & max answer.
   *
   * @param {String} aCharacteristicId -Attribut of DescriptionBO.
   * @param {String} aAnswer -Attribut of DescriptionBO.
   * @param {String} aMaxAnswer -Attribut of DescriptionBO.
   */
  constructor(aCharacteristicId, aMaxAnswer, aAnswer) {
    super();
    this.characteristic_id = aCharacteristicId;
    this.max_answer = aMaxAnswer;
    this.answer = aAnswer;
  }

  /**
   * Sets a new characteristic_id.
   *
   * @param {String} aCharacteristicId - the new characteristic_id of this DescriptionBO.
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
   * @param {*} aAnswer - the new aAnswer of this DescriptionBO.
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

  setMaxAnswer(aMaxAnswer) {
    this.max_answer = aMaxAnswer;
  }

  /**
   * Gets the About Me.
   */
  getMaxAnswer() {
    return this.max_answer;
  }

  /**
   * Returns an Array of DescriptionBOs from a given JSON structure.
   */
  static fromJSON(Descriptions) {
    let result = [];

    if (Array.isArray(Descriptions)) {
      Descriptions.forEach((u) => {
        Object.setPrototypeOf(u, DescriptionBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Descriptions;
      Object.setPrototypeOf(u, DescriptionBO.prototype);
      result.push(u);
    }

    return result;
  }
}

