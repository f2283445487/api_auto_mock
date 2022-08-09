

creat_api_info = """CREATE TABLE `api_field_info` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `API_INFO_ID` varchar(32) NOT NULL,
  `API_FIELD_NAME` varchar(32) NOT NULL,
  `API_FIELD_TYPE` varchar(32) NOT NULL,
  `API_FIELD_RANGGE` varchar(32) NOT NULL,
  `API_FIELD_DESCRIBE` varchar(32) NOT NULL,
  `API_FIELD_OPTION` varchar(32) NOT NULL,
  `API_FIELD_DEFAULT` varchar(32) NOT NULL,
  `API_FIELD_SEAT` varchar(32) NOT NULL,
  `API_FIELD_STATUS` varchar(32) NOT NULL,
  `CREAT_BY` varchar(32) NOT NULL,
  `CREAT_TIME` varchar(32) NOT NULL,
  `UPDATE_BY` varchar(32) NOT NULL,
  `UPDATE_TIME` varchar(32) NOT NULL,
  `DELETE_FG` varchar(32) NOT NULL,
  `DEFAULT` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;"""

creat_api_field_info = """CREATE TABLE `api_info` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `URL` varchar(32) NOT NULL,
  `API_NAME` varchar(32) NOT NULL,
  `API_METHOD` varchar(32) NOT NULL,
  `API_MOUDLE` varchar(32) NOT NULL,
  `API_SYSTEMS` varchar(32) NOT NULL,
  `API_DEVELOPER` varchar(32) NOT NULL,
  `CREAT_TIME` varchar(32) NOT NULL,
  `UPDATE_TIME` varchar(32) NOT NULL,
  `CREAT_BY` varchar(32) NOT NULL,
  `UPDATE_BY` varchar(32) NOT NULL,
  `DELETE_FG` varchar(32) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;"""

API_INFO = "select ID,URL,API_NAME,API_METHOD from app01_api_info"

API_FIELF_INFO = "select * from app01_api_field_info where API_INFO_ID = %s"

API_INFO_PID = "select * from app01_api_field_info where API_PID = %s "
