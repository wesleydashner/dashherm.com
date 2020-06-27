# www.dashherm.com api
This is a Django project I host on a raspberry pi that handles all the following requests:
* /make-reservation/ (POST)
    * request parameters
        * lot_id \<string\>
        * user_id \<string\>
    * response parameters
        * did_reserve \<boolean\>
* /update-reservation-status/ (POST)
    * request parameters
        * lot_id \<string\>
        * user_id \<string\>
        * status \<string\> (created, parked, parking)
    * response parameters
        * did_update \<boolean\>
* /reservable-stalls-count/ (GET)
    * request parameters
        * lot_id \<string\>
    * response parameters
        * reservable_stalls_count \<number\>
* /update-stalls/ (POST)
    * request parameters
        * lot_id \<string\>
        * statuses \<array\>
            * stall_id \<string\>
            * is_available \<boolean\>
    * response parameters
        * did_update \<boolean\>
