# -*- coding: utf-8 -*-

"""
   DigitalNewzealandLib.Models.CollectionSearchRecords
 
   This file was automatically generated by APIMATIC BETA v2.0 on 07/12/2016
"""
from DigitalNewzealandLib.APIHelper import APIHelper
from DigitalNewzealandLib.Models.ResultsCollection import ResultsCollection

class CollectionSearchRecords(object):

    """Implementation of the 'CollectionSearchRecords' model.

    Collection of search Records endpoint

    Attributes:
        num_results_requested (int): the value of the num_results parameter
            sent to the API method
        result_count (int): the total number of results matching this search
        start (string): the value of the start parameter sent to the API
            method
        results (ResultsCollection): the search results data. The results
            element will contain 0 or more result elements
        facets (dict<object, object>): the facet result data (if requested).
            The facets element will contain one facet-field element
            corresponding to each facet requested. Each facet-field element
            contains a sorted list of value elements that are made up of a
            name and num-results element. 

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the CollectionSearchRecords class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    num_results_requested -- int -- Sets the attribute num_results_requested
                    result_count -- int -- Sets the attribute result_count
                    start -- string -- Sets the attribute start
                    results -- ResultsCollection -- Sets the attribute results
                    facets -- dict<object, object> -- Sets the attribute facets
        
        """
        # Set all of the parameters to their default values
        self.num_results_requested = None
        self.result_count = None
        self.start = None
        self.results = None
        self.facets = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "num_results_requested": "num_results_requested",
            "result_count": "result_count",
            "start": "start",
            "results": "results",
            "facets": "facets",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "results" in kwargs:
                self.results = ResultsCollection(**kwargs["results"])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "num_results_requested": "num_results_requested",
            "result_count": "result_count",
            "start": "start",
            "results": "results",
            "facets": "facets",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)