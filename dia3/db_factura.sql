-- MySQL Script generated by MySQL Workbench
-- Fri Jul 12 22:40:06 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_factura
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_factura
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_factura` DEFAULT CHARACTER SET utf8 ;
USE `db_factura` ;

-- -----------------------------------------------------
-- Table `db_factura`.`tbl_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura`.`tbl_cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `razon_social` VARCHAR(255) NOT NULL,
  `ruc` VARCHAR(20) NOT NULL,
  `direccion` LONGTEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_factura`.`tbl_producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura`.`tbl_producto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `codigo` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(255) NOT NULL,
  `valor_unitario` DOUBLE NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_factura`.`tbl_factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura`.`tbl_factura` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nro_factura` VARCHAR(45) NOT NULL,
  `fecha_emision` DATE NOT NULL,
  `subtotal` DOUBLE NOT NULL,
  `igv` DOUBLE NOT NULL,
  `total` DOUBLE NOT NULL,
  `cliente_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nro_factura_UNIQUE` (`nro_factura` ASC) VISIBLE,
  INDEX `fk_tbl_factura_tbl_cliente_idx` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_tbl_factura_tbl_cliente`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `db_factura`.`tbl_cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_factura`.`tbl_factura_detalle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_factura`.`tbl_factura_detalle` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cantidad` INT NOT NULL DEFAULT 1,
  `valor_unitario` DOUBLE NOT NULL,
  `producto_id` INT NOT NULL,
  `factura_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tbl_factura_detalle_tbl_producto1_idx` (`producto_id` ASC) VISIBLE,
  INDEX `fk_tbl_factura_detalle_tbl_factura1_idx` (`factura_id` ASC) VISIBLE,
  CONSTRAINT `fk_tbl_factura_detalle_tbl_producto1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `db_factura`.`tbl_producto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_factura_detalle_tbl_factura1`
    FOREIGN KEY (`factura_id`)
    REFERENCES `db_factura`.`tbl_factura` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
