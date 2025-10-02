--local QBCore = exports['qb-core']:GetCoreObject()

local function debug(text)
    if not Config.Debug and or Config.Debug == false then return end

    print('[DEBUG] '..text)
end