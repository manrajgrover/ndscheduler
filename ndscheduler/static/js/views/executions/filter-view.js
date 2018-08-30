/**
 * executions-filter view.
 *
 * @author wenbin@nextdoor.com
 */

require.config({
  paths: {
    'jquery': 'vendor/jquery',
    'underscore': 'vendor/underscore',
    'backbone': 'vendor/backbone',
    'bootstrap': 'vendor/bootstrap',
    'moment': 'vendor/moment'
  },

  shim: {
    'bootstrap': {
      deps: ['jquery']
    },
    'backbone': {
      deps: ['underscore', 'jquery'],
      exports: 'Backbone'
    }
  }
});

define(['backbone', 'bootstrap', 'moment'], function(backbone, bootstrap, moment) {
  'use strict';

  return Backbone.View.extend({
    initialize: function() {
      $('#filter-button').on('click', _.bind(this.filterTable, this));
    },

    filterTable: function(e) {
      e.preventDefault();

      var range = $('#logs-filter-time-range').val();
      var rangeVal;
      var start;

      if (range === '*') {
        start = moment(new Date(0));
      } else {
        rangeVal = parseInt(range, 10);
        start = moment().subtract(rangeVal, 'second');
      }
      var end = moment();
      this.collection.getExecutionsByRange(start.toISOString(),
          end.toISOString());
    }
  });
});
