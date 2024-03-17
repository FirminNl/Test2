import BusinessObject from "./BusinessObject";

/**
 * Represents a Chat
 */
export default class ChatBO extends BusinessObject {
  /**
   * Constructs a ChatBO object with a given sender and receiver.
   *
   * @param {String} aSenderId -Attribut of ChatBO.
   * @param {String} aReceiverId -Attribut of ChatBO.
   * @param {boolean} aAccepted -Attribut of ChatBO.
   * @param {boolean} aIsOpen -Attribut of ChatBO.
   */
  constructor(aSenderId, aReceiverId, aAccepted, aIsOpen) {
    super();
    this.sender_id = aSenderId;
    this.receiver_id = aReceiverId;
    this.accepted = aAccepted;
    this.is_open = aIsOpen;
  }

  /**
   * Sets a new sender ID .
   *
   * @param {String} aSenderId - the new sender ID of this ChatBO.
   */
  setSenderId(aSenderId) {
    this.sender_id = aSenderId;
  }

  /**
   * Gets the sender ID.
   */
  getSenderId() {
    return this.sender_id;
  }

  /**
   * Sets a new receiver ID.
   *
   * @param {String} aReceiverId - the new receiver ID of this ChatBO.
   */
  setReceiverId(aReceiverId) {
    this.receiver_id = aReceiverId;
  }

  /**
   * Gets the ReceiverId.
   */
  getReceiverId() {
    return this.receiver_id;
  }

  /**
   * Sets a new firstname.
   * @param {Boolean} aAccepted - the new boolean value chat accepted of ChatBO
   */
  setAccepted(aAccepted) {
    this.accepted = aAccepted;
  }

  /**
   * Gets the chat accepted boolean value of chat.
   */
  getAccepted() {
    return this.accepted;
  }

  /**
   * Sets a new firstname.
   * @param {Boolean} aIsOpen - the new boolean value isopen ChatBO
   */
  setIsOpen(aIsOpen) {
    this.is_open = aIsOpen;
  }

  /**
   * Gets the is open boolean value of chat is open.
   */
  getIsOpen() {
    return this.is_open;
  }

  /**
   * Returns an Array of ChatBOs from a given JSON structure.
   */
  static fromJSON(Chats) {
    let result = [];

    if (Array.isArray(Chats)) {
      Chats.forEach((u) => {
        Object.setPrototypeOf(u, ChatBO.prototype);
        result.push(u);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let u = Chats;
      Object.setPrototypeOf(u, ChatBO.prototype);
      result.push(u);
    }

    return result;
  }
}
