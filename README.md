# Drone_models_info
An application to view and manage different drone models' info

Database details:

Database name: drone_info

Tables: 
# automation_features 
=> Like auto take-off & landing, terrain following, click & fly etc
# company
=> Like DRDO, Intel, DJI etc
# country
=> Country which macufactures it
# cv_algorithm
=> Segmentation, tracking, object detection etc
# domain
=> Agriculture, military, health etc
# drone_models
=> drone specs and relations to other tables
# pair_drone_automation_feature
=> pairwise mapping of drone with automation features that are supported in it 
# pair_drone_country
=> pairwise mapping of drone and country
# pair_drone_cv_algo
=> similar to above
# pair_drone_security_feature
=> similar to above
# security_features
=> Like encryption, alerts, back home and other security features

Main table: drone_models
Fields:
1. ID
2. Name
3. company_id. (manufacturer)
4. height
5. users (individuals or company or govt etc)
6. license (license required for using?)
7. training (training required for flying?)
8. price
9. weight_in_kg
10. country_of_operation_ID
11. domain_ID (domain of use - agriculture, military etc)
12. usecase (exact usecase within domain)
13. wingspan


# Testing
Tested all APIs using curl commands (Basic functionality testing. Special cases must be handled)
Repeated few tests on Postman - https://go.postman.co/workspace/Drone-models-details-applicatio~b949e783-b6ef-43ef-b118-d8451e02eae1/collection/19699001-fbebfd2f-5109-4d96-bd04-51b8ebbdf25d 
