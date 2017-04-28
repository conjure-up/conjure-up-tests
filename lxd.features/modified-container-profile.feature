Feature: conjure-up against a modified default lxd profile

  Scenario: Run against a profile with a zfs pool created
    Given we have a lxd profile
    When a non default zfs pool is defined
    Then conjure-up will deploy canonical-kubernetes
