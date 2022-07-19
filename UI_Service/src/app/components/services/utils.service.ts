export class Utils {
    // tslint:disable-next-line:ban-types
    static convertToLocalTime = (date: String) => {
      return !date ? '' : new Date(date + ' UTC').toLocaleString();
    }
  }
  