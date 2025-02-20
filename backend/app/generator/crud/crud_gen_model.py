#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.generator.model import GenModel
from backend.app.generator.schema.gen_model import CreateGenModelParam, UpdateGenModelParam


class CRUDGenModel(CRUDPlus[GenModel]):
    async def get(self, db: AsyncSession, pk: int) -> GenModel | None:
        """
        获取代码生成模型列

        :return:
        """
        return await self.select_model_by_id(db, pk)

    async def get_all_by_business_id(self, db: AsyncSession, business_id: int) -> Sequence[GenModel]:
        gen_model = await db.execute(
            select(self.model).where(self.model.gen_business_id == business_id).order_by(self.model.sort)
        )
        return gen_model.scalars().all()

    async def create(self, db: AsyncSession, obj_in: CreateGenModelParam, **kwargs) -> None:
        """
        创建代码生成模型表

        :param db:
        :param obj_in:
        :return:
        """
        return await self.create_model(db, obj_in, **kwargs)

    async def update(self, db: AsyncSession, pk: int, obj_in: UpdateGenModelParam, **kwargs) -> int:
        """
        更细代码生成模型表

        :param db:
        :param pk:
        :param obj_in:
        :return:
        """
        return await self.update_model(db, pk, obj_in, **kwargs)

    async def delete(self, db: AsyncSession, pk: int) -> int:
        """
        删除代码生成模型表

        :param db:
        :param pk:
        :return:
        """
        return await self.delete_model(db, pk)


gen_model_dao: CRUDGenModel = CRUDGenModel(GenModel)
