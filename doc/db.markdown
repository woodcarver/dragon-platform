```
CREATE TABLE `simulation` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(255) CHARACTER SET latin1 DEFAULT NULL COMMENT 'simulation名称',
    `profile` varchar(255) CHARACTER SET latin1 DEFAULT NULL COMMENT '星团密度分布',
    `rh` varchar(255) CHARACTER SET latin1 DEFAULT NULL COMMENT '星团半质量半径',
    `imf` varchar(255) CHARACTER SET latin1 DEFAULT NULL COMMENT '初始质量函数',
    `q` varchar(255) CHARACTER SET latin1 DEFAULT NULL COMMENT '双星质量比分布',
    `kick_ns` varchar(255) CHARACTER SET latin1 DEFAULT NULL COMMENT '中子星 kicked velocity',
    `rt` varchar(255) CHARACTER SET latin1 DEFAULT NULL COMMENT '星团潮汐半径',
    `simulation_time` bigint(20) DEFAULT NULL COMMENT '模拟产出时间',
    `publish_time` int(11) DEFAULT NULL COMMENT '发布时间',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table simulation_sample_date(
    simulation_id int,
    stellar_type int comment '星系类型',
    
) engine=innodb defualt charset=utf8;

```
