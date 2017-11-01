export class HameocPage {
  navigateTo() {
    return browser.get('/');
  }

  getParagraphText() {
    return element(by.css('hameoc-app h1')).getText();
  }
}
