CREATE TABLE `index` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录ID',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `ip` varchar(45) NOT NULL DEFAULT '' COMMENT 'ip地址，标准格式，最长格式化',
  `ua` varchar(200) DEFAULT NULL COMMENT 'user agent，超出长度取前200位',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
