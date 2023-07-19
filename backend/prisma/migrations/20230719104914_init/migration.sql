-- CreateTable
CREATE TABLE `Signal` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `ticker` VARCHAR(191) NOT NULL,
    `interval` VARCHAR(191) NOT NULL,
    `entry_date` DATETIME(3) NOT NULL,
    `out_date` DATETIME(3) NOT NULL,
    `tp` VARCHAR(191) NOT NULL,
    `sl` VARCHAR(191) NOT NULL,
    `status` VARCHAR(191) NOT NULL DEFAULT 'progress',
    `vwap21` INTEGER NOT NULL,
    `vwap48` INTEGER NOT NULL,
    `vwap84` INTEGER NOT NULL,
    `user_id` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `User` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(191) NOT NULL,
    `last_name` VARCHAR(191) NOT NULL,
    `email` VARCHAR(191) NOT NULL,
    `password` VARCHAR(191) NOT NULL,
    `phone_number` VARCHAR(191) NOT NULL,
    `telegram_id` VARCHAR(191) NOT NULL,
    `active_telegram` BOOLEAN NOT NULL DEFAULT false,
    `plan_id` INTEGER NOT NULL,
    `role` VARCHAR(191) NOT NULL,
    `signals` INTEGER NOT NULL,
    `language` VARCHAR(191) NOT NULL DEFAULT 'en',
    `theme` VARCHAR(191) NOT NULL DEFAULT 'dark',
    `api_key` VARCHAR(191) NOT NULL,
    `secret_key` VARCHAR(191) NOT NULL,
    `user_name_telegram` VARCHAR(191) NOT NULL,
    `balance_trade` INTEGER NOT NULL,

    UNIQUE INDEX `User_api_key_key`(`api_key`),
    UNIQUE INDEX `User_secret_key_key`(`secret_key`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Plan` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(191) NOT NULL,
    `description` INTEGER NOT NULL,
    `features_id` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `SignalBackTest` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `entry_date` DATETIME(3) NOT NULL,
    `out_date` DATETIME(3) NOT NULL,
    `tp` INTEGER NOT NULL,
    `sl` INTEGER NOT NULL,
    `status` INTEGER NOT NULL,
    `change` INTEGER NOT NULL,
    `vwap_value` INTEGER NOT NULL,
    `ema_value` INTEGER NOT NULL,
    `ticker_id` INTEGER NOT NULL,

    UNIQUE INDEX `SignalBackTest_ticker_id_key`(`ticker_id`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `BackTest` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `ticker` VARCHAR(191) NOT NULL,
    `interval` VARCHAR(191) NOT NULL,
    `exchange` VARCHAR(191) NOT NULL,
    `column_5` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `OnBoarding` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `image` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Feature` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(191) NOT NULL,
    `description` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `Signal` ADD CONSTRAINT `Signal_user_id_fkey` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `User` ADD CONSTRAINT `User_plan_id_fkey` FOREIGN KEY (`plan_id`) REFERENCES `Plan`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Plan` ADD CONSTRAINT `Plan_features_id_fkey` FOREIGN KEY (`features_id`) REFERENCES `Feature`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `SignalBackTest` ADD CONSTRAINT `SignalBackTest_ticker_id_fkey` FOREIGN KEY (`ticker_id`) REFERENCES `BackTest`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
