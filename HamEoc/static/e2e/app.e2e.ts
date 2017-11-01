import { HameocPage } from './app.po';

describe('hameoc App', function() {
  let page: HameocPage;

  beforeEach(() => {
    page = new HameocPage();
  })

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('hameoc works!');
  });
});
