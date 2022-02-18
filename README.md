# Drone_models_info
An application to view and manage different drone models' info

Database details:

Database name: drone_info

Tables: 
+-------------------------------+
| Tables_in_drone_info          |
+-------------------------------+
| automation_features           |.  => Like auto take-off & landing, terrain following, click & fly etc
| company                       |.  => Like DRDO, Intel, DJI etc
| country                       |.  => Country which macufactures it
| cv_algorithm                  |.  => Segmentation, tracking, object detection etc
| domain                        |.  => Agriculture, military, health etc
| drone_models                  |.  => drone specs and relations to other tables
| pair_drone_automation_feature |.  => pairwise mapping of drone with automation features that are supported in it 
| pair_drone_country            |.  => pairwise mapping of drone and country
| pair_drone_cv_algo            |.  => similar to above
| pair_drone_security_feature   |.  => similar to above
| security_features             |.  => Like encryption, alerts, back home and other security features
+-------------------------------+

Main table: drone_models
mysql> desc drone_models;
+-------------------------+--------------+------+-----+---------+-------+
| Field                   | Type         | Null | Key | Default | Extra |
+-------------------------+--------------+------+-----+---------+-------+
| ID                      | int          | NO   | PRI | NULL    |       |
| Name                    | varchar(255) | NO   |     | NULL    |       |
| company_id              | int          | NO   | MUL | NULL    |       |
| height                  | int          | YES  |     | NULL    |       |
| users                   | varchar(255) | YES  |     | NULL    |       |
| license                 | tinyint(1)   | YES  |     | NULL    |       |
| training                | tinyint(1)   | YES  |     | NULL    |       |
| price                   | int          | YES  |     | NULL    |       |
| weight_in_kg            | float        | YES  |     | NULL    |       |
| country_of_operation_ID | int          | YES  | MUL | NULL    |       |
| domain_ID               | int          | NO   | MUL | NULL    |       |
| usecase                 | varchar(255) | NO   |     | NULL    |       |
| wingspan                | float        | YES  |     | NULL    |       |
+-------------------------+--------------+------+-----+---------+-------+
13 rows in set (0.01 sec)






