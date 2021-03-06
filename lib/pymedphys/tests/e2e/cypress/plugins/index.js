/// <reference types="cypress" />
/* eslint-disable no-console */
const path = require('path')
const fs = require('fs')

// place downloads into "cypress/downloads" folder
const downloadDirectory = path.join(__dirname, '..', 'downloads')

const isFirefox = (browser) => browser.family === 'firefox'

// const {
//   addMatchImageSnapshotPlugin,
// } = require('cypress-image-snapshot/plugin');


/**
 * @type {Cypress.PluginConfig}
 */
module.exports = (on, config) => {
  // `on` is used to hook into various events Cypress emits
  // `config` is the resolved Cypress config
  // addMatchImageSnapshotPlugin(on, config);
  // register utility tasks to clear the downloads folder,
  // read and parse Excel files
  on('task', {
    clearDownloads () {
      console.log('clearing folder %s', downloadDirectory)

      fs.rmdirSync(downloadDirectory, { recursive: true })

      return null
    },


    log (message) {
      console.log(message)

      return null
    }

  })

  // https://on.cypress.io/browser-launch-api
  on('before:browser:launch', (browser, options) => {
    console.log('browser %o', browser)

    if (isFirefox(browser)) {
      options.preferences['browser.download.dir'] = downloadDirectory
      options.preferences['browser.download.folderList'] = 2

      // needed to prevent download prompt for text/csv and Excel files
      // grab the Excel MIME types by downloading the files in Excel and observing
      // the reported MIME content types in the Developer Toos
      options.preferences['browser.helperApps.neverAsk.saveToDisk'] =
        'text/csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

      return options
    }

    // note: we set the download folder in Chrome-based browsers
    // from the spec itself using automation API
  })
}
