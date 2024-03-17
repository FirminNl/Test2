import BusinessObject from "./BusinessObject";

/**
 * Represents a Message
 */
export default class MessageBO extends BusinessObject {
  /**
   * Constructs a MessageBO object with a given chat ID, sender_id, sender ID.
   *
   * @param {Integer} aChatId -Attribut of MessageBO.
   * @param {String} aContendId -Attribut of MessageBO.
   * @param {Integer} aSenderId -Attribut of MessageBO.
   */
  constructor(aChatId, aContent, aSenderId) {
    super();
    this.chat_id = aChatId;
    this.content = aContent;
    this.sender_id = aSenderId;
  }

  /**
   * Sets a Chat ID  of Message.
   *
   * @param {String} aChatId - the new Chat ID of MessageBO.
   */
  setaChatId(aChatId) {
    this.chat_id = aChatId;
  }

  /**
   * Gets the Chat ID of MessageBO.
   */
  getaChatId() {
    return this.chat_id;
  }

  /**
   * Sets a Content of Message.
   *
   * @param {String} aContend - the new Content_id of Message ID.
   */
  setContent(aContent) {
    this.content = aContent;
  }

  /**
   * Gets the Content of Message.
   */
  getContent() {
    return this.content;
  }

  /**
   * Sets a new sender ID.
   * @param {String} aSenderId - the new sender ID for MessageBO.
   */
  setSenderId(aSenderId) {
    this.sender_id = aSenderId;
  }

  /**
   * Gets the sender ID of Message.
   */
  getSenderId() {
    return this.sender_id;
  }

  /**
   * Returns an Array of MessageBOs from a given JSON structure.
   */
  static fromJSON(Messages) {
    let result = [];

    if (Array.isArray(Messages)) {
      Messages.forEach((u) => {
        Object.setPrototypeOf(u, MessageBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Messages;
      Object.setPrototypeOf(u, MessageBO.prototype);
      result.push(u);
    }

    return result;
  }
}

