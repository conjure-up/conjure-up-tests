Feature: conjure-up against custom zfs pool

  Scenario: Run against a profile with a custom zfs pool
    Given we have a lxd profile
    When a non default zfs pool is defined
    Then conjure-up will deploy canonical-kubernetes
