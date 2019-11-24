CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录ID',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `email` varchar(100) NOT NULL DEFAULT '' COMMENT '用户邮箱',
  `name` varchar(100) NOT NULL DEFAULT '' COMMENT '用户名称',
  `hashed_password` varchar(100) NOT NULL DEFAULT '' COMMENT '用户密码hash',
  `ip` varchar(45) NOT NULL DEFAULT '' COMMENT 'ip地址，标准格式，最长格式化',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
