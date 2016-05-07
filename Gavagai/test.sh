curl -v -H "Content-Type: application/json" -X POST "https://api.gavagai.se/v3/tonality?apiKey=1d3be6f17cb6d5c8ce2bc33a776d0120" -d '{
	 "language": "en",
	 "texts": [
	    {
	      "body": "West Africa is suffering the worst Ebola outbreak in history, with more than 17,100 illnesses and at least 6,000 deaths this year.",
	      "id": "http://www.kmph-kfre.com/story/27541218/american-coming-to-us-to-be-evaluated-for-ebola"
	    },
	    {
	      "body": "An American health-care worker in West Africa who may have been infected with #Ebola is being flown to Emory. West Africa is suffering the worst Ebola outbreak in history, with more than 17,100 illnesses and at least 6,000 deaths this year.",
	      "id": "https://twitter.com/DoctorYasmin/status/540277718294605824"
	    }, {
              "body": "What a wonderful, strong and moving statement by your boss. please tell her how much Sen. McCain appreciated it. Me too",
              "id": "HannesTestingStuffId1337"
            }
	  ]
	}'
