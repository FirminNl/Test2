/**
 * Base class for all BusinessObjects, which has an ID field by default.
 */
export default class BusinessObject {
  /**
   * The null constructor.
   */
  constructor() {
    this.id = 0;
    this.timestamp = new Date();
  }

  /**
   * Sets the ID of this BusinessObject.
   *
   * @param {*} aId - the new ID of this BusinessObject
   */
  setID(aId) {
    this.id = aId;
  }

  /**
   * Returns the ID of this BusinessObject.
   */
  getID() {
    return this.id;
  }

  setTimestamp(aTimestamp) {
    this.timestamp = aTimestamp;
  }

  /**
   * Returns the timestamp of this BusinessObject.
   */
  getTimestamp() {
    return this.timestamp;
  }

  /**
   * Returns a string representation of this Object. This is useful for debugging purposes.
   */
  toString() {
    let result = "";
    for (var prop in this) {
      result += prop + ": " + this[prop] + " ";
    }
    return result;
  }
}

